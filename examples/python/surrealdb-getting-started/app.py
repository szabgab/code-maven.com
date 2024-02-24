from surrealdb import Surreal
import asyncio

async def main():
    async with Surreal("ws://localhost:8000/rpc") as db:

        await db.signin({"user": "root", "pass": "root"})

        await db.use("test_namespace", "test_database")

        res = await db.create(
            "character",
            {
                "name": "Jake Sully",
                "race": "human",
            },
        )
        print(res)

        res = await db.create(
            "character",
            {
                "name": "Miles Quaritch",
                "race": "human",
            },
        )
        print(res)

        res = await db.create(
            "character",
            {
                "name": "Neytiri",
                "race": "na'vi",
            },
        )
        print(res)

        res = await db.select("character")
        print(res)

        res = await db.query("SELECT * FROM character")
        print(res)

        res = await db.query("SELECT * FROM character WHERE race='human'")
        print(res)

        res = await db.query("SELECT * FROM character WHERE race=$race", {
            'race': "na'vi",
        })
        print(res)

        #res = await db.update("character", {
        #    "race": "na'vi",
        #})

        res = await db.query("UPDATE character SET race=$race WHERE name=$name", {
            'race': "na'vi",
            'name': "Jake Sully"
        })
        print(res)

        res = await db.select("character")
        print(res)

        res = await db.delete("character")
        print(res)


asyncio.run(main())
