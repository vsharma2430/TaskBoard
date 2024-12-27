<script>
    $("#search_button").click(function (e) {
        window.open(`\?search=${$('#search_string').val()}`,"_self");
    });
</script>