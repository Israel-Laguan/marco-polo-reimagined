FROM debian:trixie-20261123-slim@sha256:8aa5a7bf5a1955bddbe7d74fcdd0b91ab30e74362a8b73af672b0481b35b44a0

ENV LANG=C.UTF-8 TZ=UTC
RUN printf '%s\n' \
    'Types: deb' \
    'URIs: http://snapshot.debian.org/archive/debian/20261124T000000Z' \
    'Suites: trixie' \
    'Components: main' \
    'Check-Valid-Until: no' \
    'Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg' \
    > /etc/apt/sources.list.d/debian.sources \
    && apt-get -o Acquire::Retries=3 update \
    && apt-get -o Acquire::Retries=3 install -y --no-install-recommends \
        biber ca-certificates chktex curl default-jre-headless fonts-dejavu-core \
        fonts-noto-cjk fonts-noto-core latexmk pandoc poppler-utils python3 python3-yaml \
        texlive-bibtex-extra texlive-latex-extra texlive-luatex unzip \
    && apt-get clean
RUN curl --fail --silent --show-error --location --retry 3 \
    https://languagetool.org/download/LanguageTool-6.6.zip --output /tmp/LanguageTool-6.6.zip \
    && echo '53600506b399bb5ffe1e4c8dec794fd378212f14aaf38ccef9b6f89314d11631  /tmp/LanguageTool-6.6.zip' | sha256sum -c \
    && unzip -q /tmp/LanguageTool-6.6.zip -d /opt \
    && unlink /tmp/LanguageTool-6.6.zip
ENV LANGUAGETOOL_JAR=/opt/LanguageTool-6.6/languagetool-commandline.jar
WORKDIR /book
