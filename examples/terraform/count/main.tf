vars {
   total = 1
}

resource "google_compute_instance" "gabor" {
  name         = "gabor-${count.index + 1}"
  machine_type = "f1-micro"
  # get the available zones of the current region and get the number of them
  #count = "${length(data.google_compute_zones.available.names)}"
  # pick the zone from the array (we cannot have a count that is larger than the available zones)
  #zone         = "${data.google_compute_zones.available.names[count.index]}"

  # we can use modulus, but now the number of entries in the list of zones is hard-coded 4
  #count        = "10"
  #zone         = "${data.google_compute_zones.available.names[count.index % 4]}"

  #vars.total = "${length(data.google_compute_zones.available.names)}"
  count        = "10"
  zone         = "${data.google_compute_zones.available.names[count.index % ${vars.total} ]}"

  labels = {
    owner = "gabor"
    group = "devops"
  }
}
