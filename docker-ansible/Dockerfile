FROM ubuntu:trusty

ENV TERM=xterm-256color

RUN sed -i "s/http:\/\/archive./http:\/\/ng.archive./g" /etc/apt/sources.list


RUN apt-get update -qy && \
    apt-get install -qy software-properties-common && \
    apt-add-repository -y ppa:ansible/ansible && \
    apt-get update -qy && \
    apt-get install -qy ansible

VOLUME [ "/ansible" ]
WORKDIR /ansible
COPY ./ansible/probe.yml /ansible/probe.yml

ENTRYPOINT [ "ansible-playbook" ]
CMD [ "site.yml" ]
