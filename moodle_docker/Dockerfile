FROM docker.io/bitnami/moodle:4.1.1

RUN install_packages openssh-client vim git unzip

ENV COMPOSER_ALLOW_SUPERUSER=1
RUN composer global config --no-plugins allow-plugins.dealerdirect/phpcodesniffer-composer-installer true
RUN composer global require moodlehq/moodle-cs --no-interaction


ENV PATH="/.composer/vendor/bin:$PATH"
