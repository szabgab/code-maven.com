function log_them() {
    var p = {
        'fname' : 'Foo',
        'lname' : 'Bar'
    };
    console.log("Before Change", p);
    p["email"] = 'foo@bar.com';
    console.log("Acter Change", p);
}

log_them();
