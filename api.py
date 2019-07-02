'''application programming interface-it helps to set a communication link b/w front end and back end or client and server
internal api's can be used without internet but web services require proper connection, every api is not web service
but evry web service has an api. '''

'''get, post, put, patch, delete

?=query parameters passed in the url of api
/=path parameter

json=java script object notation
it creates response in key value pairing
json object-key value pairing
json array contains json object

post call is used to create a resource at backend
it contains json body
post call should not have query params and path parameters because it is most acute call 
when post api is used the status code in return should be 201 in case of successful api call

put call is used to update a resource, it can contain query and path parameters 
it can have body as well but not mandatory
in case of successful put req status code =202
if in case of unavailability of resource data is created

patch is used to update existing resource at backend service
it can have both query and path param, it can have body as well
success code =202

diff b/w put and patch
patch will not create resource in case of absence
patch will only override the value for the field which is passed as a body
in case of put if we dont provide field at the field of table will be override by null

delete - to delete resource from backend systems
delete/get- status code=200

4.sx are client side servers
400 bad request
401 not authorized
404 resource not found
422 inaccessible entity

5.sx are server side errors
505 internal server error
502 bad gateway
500 server not found/accessible

3.sx are redirectional status code

amazon web services----akamai- heavy and paid source tool and cdn- open source
crud-create-post retrieve-put update-patch delete

purge(remove and upload new based on versions) the static folder and create a new one

elb(elastic load balancer)process created to handle load on website. it adds or remove servers automatically
AB-deploying a code on proportionate servers

2 libraries that helps to create api
rest- representational state transfer
soap-simple object access protocol

soap require web services descriptive language(wsdl) to connect with the server.
with help of soap we can only use xml format ,xml is more secured
tools used to run an api-postman,advance rest and soap ui

to access rest services there is no wsdl services required
in case of rest any format can be used for request response
less secured as compared to soap because of no protocol

advance rest is a plug-in in chrome and postman is also a product of google'''