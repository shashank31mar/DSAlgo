/**
 * XULSchoolChrome namespace.
 */
if ("undefined" == typeof(XULSchoolChrome)) {
  var XULSchoolChrome = {};
};

/**
 * Controls the browser overlay for the Hello World extension.
 */
XULSchoolChrome.BrowserOverlay = {
  /**
   * Says 'Hello' to the user.
   */
  sayHello : function(aEvent) {
    let stringBundle = document.getElementById("xulschoolhello-string-bundle");
    let message = stringBundle.getString("xulschoolhello.greeting.label");

    window.alert(message);
  }

  greetingShort : function(aEvent) {
  	let stringBundle = document.getElementById("xulschoolhello-string-bundle");
  	let message = stringBundle.getString("xulschoolhello.greet.short.label");
  }

  greetingMedium : function(aEvent) {
  	let stringBundle = document.getElementById("xulschoolhello-string-bundle");
  	let message = stringBundle.getString("xulschoolhello.greet.medium.label");
  }

  greetingLong : function(aEvent) {
  	let stringBundle = document.getElementById("xulschoolhello-string-bundle");
  	let message = stringBundle.getString("xulschoolhello.greet.long.label");
  }

  greetingCustom : function(aEvent) {
  	let stringBundle = document.getElementById("xulschoolhello-string-bundle");
  	let message = stringBundle.getString("xulschoolhello.greet.custom.label");
  }
};
