<template>
      <div class="search_container">
          <input 
          type="text" name="search"
          class="input_question"
          placeholder="search-question" id="search_question" @input="handleSearch($event.target.value)" />
          <div class="list_searched">
        <ul class="remove_bullet">
          <li v-for="item in searchedList" :key="item.question">
                  <a href="#" class="anchor_decoration">
                      {{ item.question }}
                  </a>
                      
          </li>
        </ul>
          </div>
      </div>
</template>
<style>
    .search_container {
        position: relative;
    }
    .list_searched {
        position: absolute;
        z-index: 6;
        top: 3rem;
        display: none;
        background: white;
        width: 400px;
    }
    .input_question:focus {
        width: 400px;
    }
    .search_container:hover .list_searched {
        display: block;
    }
</style>
<script>
import axios from 'axios';
export default {
  name: 'Search',
  data: function() {
			return {searchedList: null,}
		},
		methods: {
			handleSearch: async function(value) {
                console.log('value', value);
				const res = await axios(`http://localhost:8000/search/${value}`)
				this.searchedList = res?.data?.searched
			}
		}
}
</script>