provider "digitalocean" {
    token = "..."
}

resource "digitalocean_droplet" "web" {
    name  = "tf-1"
    image = "ubuntu-18-04-x64"
    region = "nyc1"
    size   = "512mb"
    ssh_keys = [12345]
}

output "ip" {
    value = "${digitalocean_droplet.web.ipv4_address}"
}

