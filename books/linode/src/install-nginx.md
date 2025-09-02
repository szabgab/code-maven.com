# Install nginx


* Visit: `http://IP`  (replace the IP with the real IP of your machine)
* The browser will report that it cannot find the site

* Between the command check the used disk size using `df -h` to see how much disk space is used by the Operating System and the packages.

---

* `apt update`
* `apt upgrade`
* `apt install nginx`
* `reboot`

---

* Visit: `http://IP` again (make sure it uses `http` and not `https`)


* This file `/etc/nginx/sites-enabled/default` is the configuration file of Nginx.


* Edit `/var/www/html/index.nginx-debian.html` and see the changes are reflected on the web page.


* Visit `http://IP/hello.html` and observe that the server returns a 404 page.

* Create the file `/var/www/html/404.html`
* Edit the `/etc/nginx/sites-enabled/default` file, add `	error_page      404 /404.html;`
* Reload the web server: `systemctl reload nginx`

* Visit `http://IP/hello.html` again and observe that the server returns our own 404 page.

* Create the file, `/var/www/html/hello.html` and see that it can be loaded via the browser.


