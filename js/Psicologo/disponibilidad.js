document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridWeek',
        locale: 'es',
        dayHeaderFormat: { day: '2-digit', weekday: 'long' },
        height: 500,
        slotMinTime: '08:00:00',
        slotMaxTime: '18:00:00',
        slotDuration: '01:00:00',
        slotLabelInterval: '01:00',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'timeGridWeek,timeGridDay'
        },
        editable: true, 
        selectable: true, 
        select: function(info) {
            console.log('Fecha seleccionada:', info.startStr, 'a', info.endStr);
        },
        allDaySlot: false,
        slotLabelFormat: { hour: 'numeric', minute: '2-digit', hour12: true }
    });
    calendar.render();
});

