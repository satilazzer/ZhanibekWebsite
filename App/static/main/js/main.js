let header = document.querySelector('#header');
let header_navbar = document.querySelector('.navbar')
let bottom_header = document.querySelector('.bottom_header');
let burger = document.querySelector('.header_burger');
let masters = document.querySelectorAll('.master a');
let calendar = document.querySelector('.calendar');
let date_days = document.querySelectorAll('.date_day');
let timings = document.querySelector('#timings');
let close = document.querySelector('.calendar .close');
form_ = document.querySelector('#timings .form');
select_form = document.querySelector('.select_form');
book_btn = document.querySelector('.book_btn');

burger.addEventListener('click', function(){
    bottom_header.classList.toggle('bottom_header_burger');
    header_navbar.classList.toggle('nav_list_burger');
});

const week_days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
const months = {'January': 1 , 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
let master_name;
for (let master of masters) {
    master.addEventListener('click', function(){
        let master_id_ = master.getAttribute("id");
        master_name = master_id_;
        calendar.classList.add('visible');
    });
}


for (let date_day of date_days){
    date_day.addEventListener('click', function(){
        timings.classList.add('visible');
        let data = date_day.getAttribute("id");
        let scheduleString = data.split("-").slice(4).join("-");
        let daysArray = data.split("-");
        let scheduleData = JSON.parse(scheduleString.replace(/'/g, "\""));
        let parts = data.split("-");
        let month = parts[0];
        let month_digit = months[parts[0]];
        let year = parts[1];
        let dayOfMonth = parts[2];
        weekday = daysArray[3];
        let master_data = scheduleData[master_name][week_days[daysArray[3]]];
        let form;
        if (master_data !== undefined){
            form = `
                <input type="text" value="${master_name}" name = 'master_name'>
                <p>${master_name}</p>
                <hr>
                <div class="inputs">
                    <input type="text" value="${month_digit}" name = 'month'>
                    <p>${month}</p>
                    <hr>
                    <input type="text" value="${year}" name = 'year'>
                    <p>${year}</p>
                    <hr>
                    <input type="text" value="${dayOfMonth}" name = 'dayOfMonth'>
                    <p>${dayOfMonth}</p>
                    <hr>
                    <input type="text" value="${weekday}" name = 'weekday'>
                    <p>${weekday}</p>
                </div>
                <hr>
                <p>Choose the timing: </p>`;
            let select_form_inner = ``
            for (let i of master_data) {
                let time_value = i.slice(0, 8)
                select_form_inner += `<option class = "timing" value="${time_value}">${i}</option>`;
            };
            select_form.classList.remove('none_visible');
            book_btn.classList.remove('none_visible');
            select_form.innerHTML = select_form_inner;
            form += `<input type="text" class="owner_name" placeholder="Your name:" required name = 'owner_name'>`;
        }
        else{
            select_form.classList.add('none_visible');
            book_btn.classList.add('none_visible');
            form = `<p>No slots</p>`
        }
        form_.innerHTML = form;
        console.log(dayOfMonth)
    });
};




close.addEventListener('click', function(){
    calendar.classList.remove('visible');
    timings.classList.remove('visible');
});
