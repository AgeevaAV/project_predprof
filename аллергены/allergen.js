document.addEventListener('DOMContentLoaded', function() {
    const saveButton = document.getElementById('saveButton');
    const notification = document.getElementById('notification');
    const notificationText = document.getElementById('notificationText');
    const checkboxes = document.querySelectorAll('.allergen-checkbox');
    
    // Функция для получения выбранных аллергенов
    function getSelectedAllergens() {
        const selected = [];
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                selected.push(checkbox.id);
            }
        });
        return selected;
    }
    
    // Функция для показа уведомления
    function showNotification(message) {
        notificationText.textContent = message;
        notification.classList.add('show');
        
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000);
    }
    
    // Обработчик сохранения
    saveButton.addEventListener('click', function() {
        const selectedAllergens = getSelectedAllergens();
        
        if (selectedAllergens.length === 0) {
            showNotification('Вы не выбрали ни одного аллергена');
            return;
        }
        
        // Преобразуем id в читаемые названия
        const allergenNames = {
            'fish': 'Рыба и морепродукты',
            'chicken': 'Курица и птица',
            'lactose': 'Лактоза'
        };
        
        const selectedNames = selectedAllergens.map(id => allergenNames[id]);
        
        // Показываем уведомление
        if (selectedAllergens.length === 3) {
            showNotification('Все аллергены выбраны. Будьте осторожны!');
        } else {
            showNotification(`Сохранено: ${selectedNames.join(', ')}`);
        }
        
        // Здесь можно добавить отправку данных на сервер
        console.log('Выбранные аллергены:', selectedAllergens);
        
        // Анимация кнопки
        saveButton.innerHTML = '✓ Сохранено!';
        saveButton.style.background = 'linear-gradient(135deg, #4cd964 0%, #2ecc71 100%)';
        
        setTimeout(() => {
            saveButton.innerHTML = '<span>Сохранить выбор</span>';
            saveButton.style.background = 'linear-gradient(135deg, #7e7cc1 0%, #6a67c9 100%)';
        }, 2000);
    });
    
    // анимация при клике на элементы
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const label = this.nextElementSibling;
            
            if (this.checked) {
                label.style.animation = 'none';
                setTimeout(() => {
                    label.style.animation = 'bounce 0.5s';
                }, 10);
            }
        });
    });
});