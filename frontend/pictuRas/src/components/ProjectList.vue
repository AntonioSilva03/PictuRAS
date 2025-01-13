<template>
    <div class="projects-list">
        <div class="projects-wrapper">
            <h2>All Projects</h2>
            <div class="top-projects">
                <div class="search-bar">
                    <input type="text" v-model="searchQuery" placeholder="Search in all projects..." />
                </div>
                <div class="plan-projects">
                    <p>You’re on the free plan! </p>
                    <Button1 style="margin-top: 0; margin-left: 1em;" label="Upgrade"></Button1>
                </div>
            </div>
            <table>
            <thead>
                <tr>
                    <th style="width: 5%;"><input type="checkbox" /></th>
                    <th style="width: 50%;">Title</th>
                    <th style="width: 25%;">Last Modified</th>
                    <th style="width: 20%;">Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="project in filteredProjects" :key="project.id">
                    <td><input type="checkbox" /></td>
                    <td>{{ project.title }}</td>
                    <td>{{ project.lastModified }}</td>
                    <td class="actions">
                        <FontAwesomeIcon :icon="['fas', 'download']" title="Download" class="action-icon" />
                        <FontAwesomeIcon :icon="['fas', 'edit']" title="Edit" class="action-icon" />
                        <FontAwesomeIcon :icon="['fas', 'eye']" title="View" class="action-icon" />
                        <FontAwesomeIcon :icon="['fas', 'trash']" title="Delete" class="action-icon" />
                    </td>
                </tr>
            </tbody>
        </table>
        <p class="footer">Showing {{ filteredProjects.length }} out of {{ projects.length }} projects.</p>
        </div>
    </div>
</template>


<script>
import Button1 from '../components/Button-style1.vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faDownload, faEdit, faEye, faTrash } from '@fortawesome/free-solid-svg-icons';
import { library } from '@fortawesome/fontawesome-svg-core';

library.add(faDownload, faEdit, faEye, faTrash);

export default {
    name: "ProjectsList",
    components:{
        Button1,
        FontAwesomeIcon,
    },
    data() {
        return {
            searchQuery: "",
            projects: [
                { id: 1, title: "ASCN TP",lastModified: "8 days ago" },
            ],
        };
    },
    computed: {
        filteredProjects() {
            return this.projects.filter((project) =>
                project.title.toLowerCase().includes(this.searchQuery.toLowerCase())
            );
        },
    },
}


</script>

<style scoped>
    .projects-list {
    width: 83%;
    align-self: flex-end;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 5px;
    border: 1px solid #ddd;
    flex: 1;
    overflow-y: auto; 
    
}

.projects-wrapper{
    display: flex;
    flex-direction: column;
    align-self: center;
    padding: 20px;
    width: 95%;
    height: 100%;
}

.top-projects{
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    align-items: center;
    width: 90%;
    align-self: center;
    margin-bottom: 4em;
}

.plan-projects{
    display: flex;
    flex-direction: row;
    align-items: center;
}

h2 {
    font-size: 1.5em;
    margin-bottom: 10px;
    color: #333;
    margin-left: 5%
}

.search-bar {
    width: 60%;
}

.search-bar input {
    width: 50%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

table {
    width: 70%;
    align-self: center;
    border-collapse: collapse;
    margin-bottom: 20px;
}

thead {
    background-color: #f9f9f9;
}

th, td {
    text-align: left;
    padding: 10px;
    border: 1px solid #ddd;
}

th {
    font-weight: bold;
    color: #555;
}

td.actions {
    display: flex;
    gap: 10px;
}

.action-icon {
    font-size: 1.2em; 
    cursor: pointer; 
    color: #555; 
    transition: color 0.3s ease-in-out; 
}

.action-icon:hover {
    color: #ff6600c2; 
    cursor: pointer; 
}


.footer {
    font-size: 0.9em;
    color: #555;
    align-self: center;
}

</style>