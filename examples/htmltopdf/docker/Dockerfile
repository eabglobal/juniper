FROM lambci/lambda:build-python3.6

# Upgrade packages & repo
RUN yum -y update
# wkhtmltopdf's dependencies
RUN yum -y install zlib fontconfig freetype libX11 libXext libXrender wget

# Download x64 static build of wkhtmltox (with patched QT)
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz

RUN tar vxf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz

RUN mkdir -p /var/task/lambda_bin/
RUN cp wkhtmltox/bin/wk* /var/task/lambda_bin/
RUN cp wkhtmltox/bin/wk* /usr/local/bin/
