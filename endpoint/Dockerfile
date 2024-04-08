FROM ontop/ontop
WORKDIR /opt/ontop
COPY input/ontology.ttl input/ontology.obda input/ontology.properties input/
COPY jdbc/h2-1.4.196.jar jdbc/
EXPOSE 8080
ENTRYPOINT java -cp ./lib/*:./jdbc/* -Dlogback.configurationFile=file:./log/logback.xml \
        it.unibz.inf.ontop.cli.Ontop endpoint \
        --ontology=input/ontology.ttl \
        --mapping=input/ontology.obda \
        --properties=input/ontology.properties \
        --cors-allowed-origins=http://yasgui.org
