// код вышел не оч, поэтому как дойдешь до него - можешь менять все, что хочешь!!
 const ratingsData = [
            {
                id: 1,
                orderNumber: 'Заказ №001',
                rating: 5,
                dishes: '???'
            },
            {
                id: 2,
                orderNumber: 'Заказ №002',
                rating: 4,
                dishes: '???'
            },
            {
                id: 3,
                orderNumber: 'Заказ №003',
                rating: 3,
                dishes: '???'
            },
            
        ];

        function renderRatings() {
            const ratingsList = document.getElementById('ratings-list');
            ratingsList.innerHTML = '';

            ratingsData.forEach(rating => {
                const ratingCard = document.createElement('div');
                ratingCard.className = 'rating-card';
                ratingCard.dataset.id = rating.id;

                // Создаем звезды
                let starsHtml = '';
                for (let i = 1; i <= 5; i++) {
                    if (i <= rating.rating) {
                        starsHtml += '<span class="star-filled">★</span>';
                    } else {
                        starsHtml += '<span class="star-empty">★</span>';
                    }
                }

                ratingCard.innerHTML = `
                    <div class="rating-header">
                        <div class="order-number">${rating.orderNumber}</div>
                        <div class="order-date">${rating.date}</div>
                    </div>
                    <div class="rating-stars">
                        ${starsHtml}
                    </div>
                    <div class="order-dishes">
                        ${rating.dishes}
                    </div>
                    <button class="delete-btn" onclick="deleteRating(${rating.id})">
                        Удалить оценку
                    </button>
                `;

                ratingsList.appendChild(ratingCard);
            });
        }

        function deleteRating(id) {
            if (confirm('Вы уверены, что хотите удалить эту оценку?')) {
                // В реальном приложении здесь будет запрос к серверу
                const index = ratingsData.findIndex(rating => rating.id === id);
                if (index !== -1) {
                    ratingsData.splice(index, 1);
                    renderRatings();
                    showNotification('Оценка удалена');
                }
            }
        }

        function showNotification(message) {
            const notification = document.


getElementById('notification');
            const notificationText = document.getElementById('notificationText');
            
            notificationText.textContent = message;
            notification.classList.add('show');
            
            setTimeout(() => {
                notification.classList.remove('show');
            }, 3000);
        }

        // Инициализация
        document.addEventListener('DOMContentLoaded', renderRatings);