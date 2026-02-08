document.addEventListener('DOMContentLoaded', function() {
    const saveButton = document.getElementById('saveButton');
    const notification = document.getElementById('notification');
    const notificationText = document.getElementById('notificationText');
    const checkboxes = document.querySelectorAll('.allergen-checkbox');
    
    saveButton.addEventListener('click', function() {
        const selectedAllergens = [];
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                selectedAllergens.push(checkbox.id);
            }
        });
        
        if (selectedAllergens.length === 0) {
            notificationText.textContent = 'Вы не выбрали ни одного аллергена';
        } else {
            notificationText.textContent = 'Выбор сохранен успешно!';
        }
        
        notification.classList.add('show');
        
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000);
        
        console.log('Выбранные аллергены:', selectedAllergens);
    });
});