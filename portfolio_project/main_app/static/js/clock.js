function updateMyClock() {
    const myTimeZone = "Europe/Vilnius";
    const now = new Date();
    const options = { timeZone: myTimeZone };
    const formattedTime = now.toLocaleTimeString("en-GB", options);
    const formattedDate = now.toLocaleDateString("en-GB", options);
    const myTimeElement = document.getElementById("my-time");
    myTimeElement.innerHTML = `<div>${formattedDate}</div><div>${formattedTime}</div>`;
  }
  
  function updateYourClock() {
    const now = new Date();
    const formattedTime = now.toLocaleTimeString("en-GB");
    const formattedDate = now.toLocaleDateString("en-GB");
    const yourTimeElement = document.getElementById("your-time");
    yourTimeElement.innerHTML = `<div>${formattedDate}</div><div>${formattedTime}</div>`;
  }

  setInterval(updateMyClock, 1000);
  setInterval(updateYourClock, 1000);
  
  updateMyClock();
  updateYourClock();