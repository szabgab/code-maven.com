function log_them() {
    var p = {
        'fname' : 'Foo',
        'lname' : 'Bar'
    };
    console.log("Before Change", JSON.parse(JSON.stringify(p)));
    p["email"] = 'foo@bar.com';
    console.log("Acter Change", JSON.parse(JSON.stringify(p)));

}

log_them();
