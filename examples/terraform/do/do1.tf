provider "digitalocean" {
    token = "..."
}

resource "digitalocean_droplet" "web" {
    name  = "tf-1"
    image = "ubuntu-18-04-x64"
    region = "nyc1"
    size   = "512mb"
}
