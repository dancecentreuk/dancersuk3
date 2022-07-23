// //Create function to select elements
// const selectElement = (element) => document.querySelector(element);
//
//
// //Open and close nav on click
//
// selectElement('.menu-icons').addEventListener('click',()=> {
//     selectElement('nav').classList.toggle('active');
// });




//Create function to select elements
const selectElement = (element) => document.querySelector(element);


//Open and close nav on click

selectElement('.menu-icons').addEventListener('click',()=> {
    selectElement('nav').classList.toggle('active');
});


// const btns = document.querySelectorAll("[data-target]")
// const close_btns = document.querySelectorAll(".modal-btn")
// const overlay = document.querySelector("#overlay")

// btns.forEach(btn => {
//     btn.addEventListener('click', ()=> {
//         document.querySelector(btn.dataset.target).classList.add("active");
//         overlay.classList.add("active")
//     })
// })
//
// close_btns.forEach(btn => {
//     btn.addEventListener('click', ()=> {
//         document.querySelector(btn.dataset.target).classList.remove("active");
//         overlay.classList.remove("active")
//     })
// })
//
//
// window.onclick = (e) => {
//     if(e.target == overlay){
//         const modals = document.querySelectorAll('.modal');
//         modals.forEach(modal => modal.classList.remove('active'))
//         overlay.classList.remove("active")
//     }
// }
//


const modalTriggerButtons = document.querySelectorAll("[data-modal-target]");
const modals = document.querySelectorAll(".modal");
const modalCloseButtons = document.querySelectorAll(".modal-close");
const modalCancelButtons = document.querySelectorAll(".modal-cancel");


modalTriggerButtons.forEach(elem => {
    elem.addEventListener("click", event => toggleModal(event.currentTarget.getAttribute("data-modal-target")));
});


modalCloseButtons.forEach(elem =>{
    elem.addEventListener("click", event => toggleModal(event.currentTarget.closest(".modal").id));
});

modalCancelButtons.forEach(elem =>{
    elem.addEventListener("click", event => toggleModal(event.currentTarget.closest(".modal").id));
});


modals.forEach(elem => {
    elem.addEventListener("click", event => {
        if(event.currentTarget===event.target) toggleModal(event.currentTarget.id)
    });

});







function toggleModal(modalId) {

    const modal = document.getElementById(modalId);




    if(getComputedStyle(modal).display==="flex"){
        modal.classList.add("modal-hide");
        setTimeout(() => {
            modal.style.display = "none";
            modal.classList.remove("modal-show", "modal-hide");
            document.body.style.overflow = "initial";

        }, 500)

    }
    else {
        modal.style.display = "flex";
        modal.classList.add("modal-show");
        document.body.style.overflow = "hidden";
    }
}





setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);






