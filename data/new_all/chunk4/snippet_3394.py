# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74933471/type-error-and-got-an-unexpected-keyword-argument-when-passing-dict-to-python-z
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xmltodict
    _l_(602260)

except ImportError:
    pass
try:
    import pprint
    _l_(602262)

except ImportError:
    pass
try:
    import json
    _l_(602264)

except ImportError:
    pass

my_xml = """
          <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsu="http://www.docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
   <soapenv:Header/>
   <soapenv:Body>
      <RequestMessage xmlns="http://www.ercot.com/schema/2007-06/nodal/ews/message">
         <Header>
            <Verb>create</Verb>
            <Noun>OutageSet</Noun>
            <ReplayDetection>
               <Nonce>72465</Nonce>
               <Created>2022-12-27T00:40:00-07:00</Created>
            </ReplayDetection>
            <Revision>004</Revision>
            <Source>TAEPTC</Source>
            <!--Optional:-->
            <UserID>API_OutplanOSITCC</UserID>
         </Header>
         <Payload>
            <OutageSet xmlns="http://www.ercot.com/schema/2007-06/nodal/ews">
               <Outage>
                  <OutageInfo>
                     <outageType>PL</outageType>
                     <Requestor>
                        <name>API_OutplanOSITCC</name>
                        <userFullName>APIOutplanOSITCC</userFullName>
                     </Requestor>
                     <Disclaimer>tempdisclaimer</Disclaimer>
                     <disclaimerAck>true</disclaimerAck>
                  </OutageInfo>
                  <TransmissionOutage>
                     <operatingCompany>TAEPTC</operatingCompany>
                     <equipmentName>1589</equipmentName>
                     <equipmentIdentifier>_{072D6FCA-D121-49E7-AC9D-CDF5D4DB3D70}</equipmentIdentifier>
                     <transmissionType>DSC</transmissionType>
                     <fromStation>AIRLINE</fromStation>
                     <outageState>O</outageState>
                     <emergencyRestorationTime>1</emergencyRestorationTime>
                     <natureOfWork>OE</natureOfWork>
                  </TransmissionOutage>
                  <Schedule>
                     <plannedStart>2023-01-16T10:00:00</plannedStart>
                     <plannedEnd>2023-01-17T10:00:00</plannedEnd>
                     <earliestStart>2023-01-16T10:00:00</earliestStart>
                     <latestEnd>2023-01-17T12:00:00</latestEnd>
                  </Schedule>
               </Outage>
            </OutageSet>
         </Payload>
      </RequestMessage>
   </soapenv:Body>
</soapenv:Envelope>
   


"""
_l_(602265)
my_dict = _c_(602269, _a_(602267, _n_(602266, "xmltodict", lambda: xmltodict), "parse"), _n_(602268, "my_xml", lambda: my_xml), process_namespaces= True)
_l_(602270)
#pp = pprint.PrettyPrinter(indent=2)
_c_(602273, _n_(602271, "print", lambda: print), _n_(602272, "my_dict", lambda: my_dict))
_l_(602274)