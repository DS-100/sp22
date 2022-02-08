/*
 * Lots of credit to CS 61A - cs61a.org
 */
const startDate = "2019-01-22",
  endDate = "2019-05-17";

// Show the current week during the semester and the first week of class otherwise.
function calendarStartDate() {
  if (
    moment().isBefore(moment(endDate)) &&
    moment().isAfter(moment(startDate))
  ) {
    return moment();
  }
  return startDate;
}

function transform(event) {
  delete event.url;
  return event;
}

function render(event, element, _) {
  let eventStr = "";
  if (typeof event.location != "undefined") {
    eventStr = "@ " + event.location;
  }
  element.append($('<div class="fc-content">').html(eventStr));
  if (event.title.includes("Lecture")) {
    element.addClass("lecture-event");
  }
  if (event.title.includes("Exam Prep") || event.title.includes("Challenge")) {
    element.addClass("special-section-event");
  }
  if (event.title.includes("LOST")) {
    element.addClass("lost-section-event");
  }
  if (event.title.includes("Josh Hug")) {
    element.addClass("hug-event");
  }

  eventStr = "";
  if (typeof event.description != "undefined") {
    eventStr =
      "<b>" +
      event.title +
      "</b> <br>" +
      event.description.split("\n").join("<br>");
  } else if (typeof event.location != "undefined") {
    eventStr = event.title + " @ " + event.location;
  }

  tippy(element[0], {
    content: eventStr,
    followCursor: true,
    animation: "fade",
    boundary: "viewport",
    theme: "light",
    animateFill: false,
    livePlacement: false
  });
}

function launchCal(lab_disc_url, oh_url) {
  return function() {
    $("#lab_disc").fullCalendar({
      allDaySlot: false,
      defaultView: "agendaWeek",
      hiddenDays: [6, 7],
      slotEventOverlap: false,
      height: "auto",
      minTime: "09:00:00",
      maxTime: "21:00:00",
      defaultDate: calendarStartDate(),
      eventDataTransform: transform,
      eventRender: render,
      googleCalendarApiKey: "AIzaSyDgOiy-PbgwzyEA9hUVQVayKMHQcDqFhXw",
      eventSources: [
        {
          googleCalendarId: lab_disc_url,
          cache: true
        }
      ]
    });
    $("#oh").fullCalendar({
      allDaySlot: false,
      defaultView: "agendaWeek",
      slotEventOverlap: false,
      height: "auto",
      minTime: "09:00:00",
      maxTime: "21:00:00",
      defaultDate: calendarStartDate(),
      eventDataTransform: transform,
      eventRender: render,
      googleCalendarApiKey: "AIzaSyDgOiy-PbgwzyEA9hUVQVayKMHQcDqFhXw",
      eventSources: [
        {
          googleCalendarId: oh_url,
          cache: true
        }
      ]
    });

    resizeCal();
    $(window).resize(resizeCal);
  };
}

function resizeCal() {
  if ($(window).width() < 900) {
    $("#oh").fullCalendar("changeView", "agendaDay");
    $("#lab_disc").fullCalendar("changeView", "agendaDay");
  } else {
    $("#oh").fullCalendar("changeView", "agendaWeek");
    $("#lab_disc").fullCalendar("changeView", "agendaWeek");
  }
}
