// Client ID and API key from the Developer Console
var CLIENT_ID = '18314785659-jujmftt3vdcfu2ipgb062jst513lg0gb.apps.googleusercontent.com';
var API_KEY = 'AIzaSyAarPsuuFGMk5QM9hMf-X05tMVktpuD-5o';

// Array of API discovery doc URLs for APIs used by the quickstart
var DISCOVERY_DOCS = ["https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest"];

// Authorization scopes required by the API; multiple scopes can be
// included, separated by spaces.
var SCOPES = "https://www.googleapis.com/auth/calendar";


/**
 *  On load, called to load the auth2 library and API client library.
 */
var listOfEventsExternal=null;
function handleClientLoad() {
    gapi.load('client:auth2', initClient);
}

/**
 *  Initializes the API client library and sets up sign-in state
 *  listeners.
 */
function initClient() {
    gapi.client.init({
        apiKey: API_KEY,
        clientId: CLIENT_ID,
        discoveryDocs: DISCOVERY_DOCS,
        scope: SCOPES
    }).then(function () {
        // Listen for sign-in state changes.
        gapi.auth2.getAuthInstance().isSignedIn.listen(updateSigninStatus);
    });
}
function handleAllGcal(stringifiedEvents){
    console.log(stringifiedEvents);
    listOfEventsExternal=stringifiedEvents;
    handleSignoutClick();
    handleAuthClick();
    //gapi.auth2.getAuthInstance().isSignedIn.listen(updateSigninStatus);
    updateSigninStatus(gapi.auth2.getAuthInstance().isSignedIn.get());
    console.log('done signing in');
    //insertSampleEvent();
}

/**
 *  Called when the signed in status changes, to update the UI
 *  appropriately. After a sign-in, the API is called.
 */
function updateSigninStatus(isSignedIn) {
    console.log('in sign in function');

        insertSampleEvent();
}

/**
 *  Sign in the user upon button click.
 */
function handleAuthClick(event) {
    gapi.auth2.getAuthInstance().signIn();
    console.log('in auth function');
}

/**
 *  Sign out the user upon button click.
 */
function handleSignoutClick(event) {
    gapi.auth2.getAuthInstance().signOut();
    console.log('in signout function');
}



function insertSampleEvent(){
    console.log('in insert function');
    console.log(listOfEventsExternal);

    /*var listOfEventsParsed=JSON.parse(listOfEventsExternal);
    for(var i=0;i<listOfEventsParsed.length;i++){
           var eventElem = listOfEventsParsed[i];        

        var request = gapi.client.calendar.events.insert({
            'calendarId': 'primary',
            'resource': eventElem
        });
        console.log('request')

            request.execute(function(event) {
                console.log('executing insertion')
            });
    
    }
    */
    var sampleEvent= {
        'summary': 'Google I/O 2015',
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2018-03-29T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2018-03-29T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        }

    }
    var request = gapi.client.calendar.events.insert({
            'calendarId': 'primary',
            'resource': sampleEvent
        });
        console.log('request')

            request.execute(function(event) {
                console.log('executing insertion')
            });
}


