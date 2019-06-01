#!/usr/bin/env bash
yum install libxml2-devel xmlsec1-devel xmlsec1-openssl-devel libtool-ltdl-devel -y

cp /usr/lib64/libxmlsec1-openssl.so ./lambda_lib/
cp /usr/lib64/libxmlsec1.so.1 ./lambda_lib/