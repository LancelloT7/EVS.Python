function toggleSidebar() {
    var sidebar = document.getElementById("mySidebar");
    var content = document.querySelector(".main-content");

    sidebar.classList.toggle("collapsed");
    content.classList.toggle("collapsed");
}
