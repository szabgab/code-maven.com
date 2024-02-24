from surrealdb import Surreal
import asyncio
import sys

async def main():

    async with Surreal("ws://localhost:8000/rpc") as db:

        await db.signin({"user": "root", "pass": "root"})

        await db.use("code-maven", "phonebook")

        await db.query("DEFINE INDEX people_name ON TABLE people COLUMNS name UNIQUE")

        if len(sys.argv) == 1:
            usage()

        action = sys.argv[1]

        if action == "list":
            res = await db.query("SELECT * FROM people ORDER BY name")
            # print(res)
            for entry in res[0]['result']:
                # print(entry)
                print(f"{entry['name']}   {entry['phone']}")
            return

        if action == "add":
            if len(sys.argv) != 4:
                usage()
            (name, phone) = sys.argv[2:4]
            try:
                res = await db.create("people", {
                    'name': name,
                    'phone': phone,
                })
                print(res)
            except Exception as err:
                print(f"Exception: {err}")
                # surrealdb.ws.SurrealPermissionException: There was a problem with the database: Database index `people_name` already contains 'foo', with record
            return

        if action == "show":
            if len(sys.argv) != 3:
                usage()
            name = sys.argv[2]

            res = await db.query("SELECT * FROM people WHERE name=$name", {
                'name': name,
            })
            if len(res[0]["result"]) == 0:
                print(f"Could not find '{name}'");
            if len(res[0]["result"]) > 1:
                print("More than 1 found")
            for entry in res[0]['result']:
                print(f"{entry['name']}   {entry['phone']}")
            return

        if action == "delete":
            if len(sys.argv) != 3:
                usage()
            name = sys.argv[2]
            res = await db.query("DELETE FROM people WHERE name=$name", {
                'name': name,
            })
            print(res)
            return

        if action == "update":
            if len(sys.argv) != 4:
                usage()
            (name, phone) = sys.argv[2:4]
            res = await db.query("UPDATE people SET phone=$phone WHERE name=$name", {
                'name': name,
                'phone': phone,
            })
            if len(res[0]["result"]) == 0:
                print(f"Could not find '{name}'");
            else:
                print(res)
            return

        usage()


def usage():
    exit(f"""Usage: {sys.argv[0]}
               add NAME PHONE
               show NAME
               update NAME PHONE
               delete NAME
               list
""")


asyncio.run(main())
