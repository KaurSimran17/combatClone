let nextBtn = document.getElementById("next_btn");
let changePage = document.getElementById("changePage");
let selectValue = document.getElementById("select_value")
nextBtn.addEventListener("click", () => {
    let list1 = document.getElementById("list");
    values = list1.value;
    if (values == "") {
        // selectValue.innerHTML = "Please select your role"
        alert("Please select your role")
    }
    else if (values == "fighter") {
        changePage.href = "fighter.html"
    }
    else {
        changePage.href = "register.html"
    }
})

