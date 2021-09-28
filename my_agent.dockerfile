FROM jetbrains/teamcity-minimal-agent
USER root
RUN apt update && \
apt install -y wget gnupg
RUN wget https://raw.githubusercontent.com/pytest-dev/execnet/master/execnet/script/socketserver.py && \
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
python3-requests \
openjdk-8-jre-headless && \
dpkg -i *.deb && \
rm -rf *.deb && \
pip3 install --system allure-pytest && \
pip3 install --system pytest-xdist 
COPY run.sh /home/buildagent/
RUN chmod a+x /home/buildagent/run.sh && \
chmod -R 755 /usr/share/allure
RUN echo 'buildagent ALL=NOPASSWD: /usr/bin/find, /usr/bin/sed' >> /etc/sudoers && \
mv socketserver.py /home/buildagent/
USER buildagent
RUN PATH=/home/buildagent/.local/bin:$PATH && \
pip3 install geckodriver-autoinstaller chromedriver-binary-auto declxml
USER root
CMD /home/buildagent/run.sh



