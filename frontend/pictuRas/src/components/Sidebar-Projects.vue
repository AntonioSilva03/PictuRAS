<template>
    <div class="sidebar">
        <div class="sidebar-container1">
            <img src="../assets/logo.png">
            <h2>PictuRAS</h2>
        </div>
        <Button1 label="New Project"></Button1>

        <!-- Menu Section -->
        <ul class="menu">
            <li 
                :class="{ active: activeItem === 'All Projects' }"
                @click="setActive('All Projects')"
            >
                All Projects
            </li>
            <li 
                :class="{ active: activeItem === 'Archived Projects' }"
                @click="setActive('Archived Projects')"
            >
                Archived Projects
            </li>
            <li 
                :class="{ active: activeItem === 'Trashed Projects' }"
                @click="setActive('Trashed Projects')"
            >
                Trashed Projects
            </li>
            <hr>
        </ul>

          <!-- Favorites Section -->
        <div class="favorites-section">
            <h3>Favorites</h3>
            <button class="new-tag-btn">+   Add Favorite</button>
            <hr>
        </div>

        <!-- Feedback Section -->
        <div class="feedback-section">
            <h3>We want your feedback</h3>
            <p>Tell us what you think about our latest projects homepage update.</p>
            <button class="take-survey-btn">Take survey</button>
        </div>

        <!-- Bottom Icons -->
        <div class="bottom-icons">
            <button class="help-btn" title="Help">❓</button>
            <button class="profile-btn" title="Profile">👤</button>
        </div>
        
       
    </div>
</template>


<script>
import Button1 from '../components/Button-style1.vue';

export default {
    name: 'SidebarProjects',
    components: {
        Button1

    },

    data() {
        return {
            activeItem: 'All Projects', // Define o item ativo inicial
        };
    },
    methods: {
        setActive(item) {
            this.activeItem = item; // Atualiza o item ativo
        },
    },
};
</script>

<style scoped>

.sidebar {
    background-color: #ffffff;
    border-right: 1px solid #ddd;
    padding: 20px;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    height: 100vh;
    max-height: 100vh;
    position: fixed;
    width: 13%;
    display: flex;
    align-items: center;
    flex-direction: column;
    min-width: 150px
}

.sidebar-container1{
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 70%;
    margin-bottom: 1em;
    align-self: flex-start;
}

.sidebar-container1 img{
    width: 50px;
    height: 50px;
}

.sidebar h2 {
    font-size: 1.3em;
    color: #333;
}

.menu {
    list-style: none;
    padding: 0;
    margin-top: 2em;
    width: 90%;
    align-self: flex-start;
}

.menu li {
    padding: 10px 15px;
    width: 85%;
    cursor: pointer;
    color: #555;
    border-radius: 5px;
    margin: 5px 0;
    transition: background-color 0.3s, color 0.3s;
}

.menu li:hover {
    background-color: #f1f1f1;
    color: #000;
}

.menu li.active {
    background-color: #ffdc7a; 
    color: #000000; 
    font-weight: bold;
}

hr{
    margin-top: 2em;
}

.favorites-section{
    width: 90%;
    align-items: flex-start;
    padding: 0;

}


.favorites-section h3 {
    font-size: 1em;
    color: #333;
    margin-bottom: 15px;
    align-self: flex-start;
}

.new-tag-btn {
    background-color: transparent;
    border: 1px solid transparent;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 5px;
    font-size: 1em;
    width: 100%;
    text-align: start;
    transition: background-color 0.3s, color 0.3s;
}

.new-tag-btn:hover {
    color: #000000;
    background-color: #55555544;
}

.feedback-section {
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    padding: 15px;
    width: 90%;
    border-radius: 5px;
    margin-top: 20px;
}

.feedback-section h3 {
    font-size: 1em;
    color: #333;
    margin-bottom: 10px;
}

.feedback-section p {
    font-size: 0.9em;
    color: #555;
    margin-bottom: 10px;
}

.take-survey-btn {
    background-color: #ffffff;
    border: 1px solid #ddd;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 2em;
    transition: border-color 0.3s, background-color 0.3s, color 0.3s;
}

.take-survey-btn:hover {
    background-color: #ffdc7a;
    color: #000000;
}

.bottom-icons {
    display:flex;
    gap: 10px;
    margin-top: 60%;

}

.help-btn,
.profile-btn {
    background-color: transparent;
    border: 1px solid grey;
    font-size: 1.2em;
    padding: 10px;
    border-radius: 50%;
    cursor: pointer;
    transition: color 0.3s;
}

.help-btn:hover,
.profile-btn:hover {
    color: #28a745;
    border: 1px solid #ffdc7a;
}


</style>