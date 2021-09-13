FROM jetbrains/teamcity-minimal-agent
USER root
RUN apt update && \
apt dist-upgrade -y && \
apt install -y wget gnupg && \
wget https://github.com/allure-framework/allure2/releases/download/2.14.0/allure_2.14.0-1_all.deb && \
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
apt update && \
apt install -y \
sudo \
google-chrome-stable \
firefox \
python3.9 \
python3-pytest \
python3-pip \
python3-selenium \
openjdk-8-jre-headless && \
dpkg -i *.deb && \
rm -rf *.deb && \
pip3 install --system geckodriver-autoinstaller chromedriver-binary-auto


