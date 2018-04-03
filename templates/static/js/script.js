/*function to get the user credentials
 * returns the credentials as an object
 * returns false if the credentials are incorrect
 * */
function retrieveCredentials(){
    var username = $("#ssousername").val();
    var password = $("#ssopassword").val();
    if(isEmpty(username)||isEmpty(password))
        return false;
    var credentials={}
    credentials.username = username;
    credentials.password = password;
    return credentials;
}
/* function to handle the user submit  */
function submitForm(){
    var credentials = retrieveCredentials();
    if(credentials==false){
        displayLoginError();
    }
    else
        sendCredentialsToPython(credentials)
}
/*function to check whether strin is empty */
function isEmpty(str) {
    return (!str || 0 === str.length);
}
/* display error message on screen */
function displayLoginError(){
    alert("Incorrect Login-Credentials");
}
//i put the sendCredentialsToPython in the index html because it was easier for the paths

