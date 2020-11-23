#!/bin/bash

set -eu -o pipefail

image="${CI_REGISTRY_IMAGE:-perl-builder}"
tag="${CI_COMMIT_REF_SLUG:-latest}"

echo "Building $image:$tag"

ctr=$(buildah from docker.io/perl:5.30)

buildah config \
  --author='Ioan Rogers <ioan@rgrs.ca>' \
  --workingdir=/src \
  --env='PERL_CPANM_OPT=--notest --no-man-pages' \
$ctr

function brun() {
  buildah run $ctr -- "$@"
}

brun cpanm App::cpm
brun cpm install -g \
	Dist::Zilla \
	Dist::Zilla::App::Command::cover \
	Devel::Cover::Report::Kritika \
	TAP::Formatter::JUnit

brun apt-get clean
brun rm -rf /root/.cpanm /root/.perl-cpm

buildah commit --rm $ctr "$image:$tag"
