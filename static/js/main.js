// Wait for the document to be ready
$(document).ready(function() {
    
    [cite_start]// Use jQuery for event handling [cite: 11]
    $('#aircraft-form').on('submit', function(event) {
        
        // Get the selected value from the dropdown
        const selectedAircraft = $('#aircraft-select').val();
        
        [cite_start]// Perform form validation [cite: 10]
        if (!selectedAircraft) {
            // Prevent the form from submitting
            event.preventDefault(); 
            
            [cite_start]// Use jQuery for a small UI effect (showing an error message) [cite: 11]
            $('#error-message').show();
        } else {
            // If valid, make sure the error message is hidden
            $('#error-message').hide();
        }
    });
});