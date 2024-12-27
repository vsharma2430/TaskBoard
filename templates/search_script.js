<script>
    let search_form = document.getElementById("search_form");

    search_form.addEventListener("submit", (e) => {
        e.preventDefault();
        window.open('?search='+$("#search_string").val(),'_self');
    });
</script>