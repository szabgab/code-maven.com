#!/usr/bin/env perl
use JSON qw(decode_json);
print JSON->new->ascii->pretty->encode(decode_json join '', <>);
