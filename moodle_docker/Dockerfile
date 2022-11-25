FROM docker.io/bitnami/moodle:4

RUN install_packages openssh-client vim git unzip

ENV COMPOSER_ALLOW_SUPERUSER=1
COPY ./composer.json /.composer/
RUN composer global update

ENV PATH="/.composer/vendor/bin:$PATH"
