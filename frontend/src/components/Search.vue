<template>
  <div class="search_container">
    <input
      type="text"
      name="search"
      class="search_question"
      placeholder="Search by question"
      autocomplete="off"
      @input="handleSearch($event.target.value)"
    />
    <div class="list_searched" v-if="searchedList">
      <ul class="remove_bullet">
        <li v-for="item in searchedList" :key="item.question">
          <button class="link_button" @click="handleSearchClick(item.id)">{{item.question}}</button>
        </li>
      </ul>
    </div>
  </div>
</template>
<style>
.search_question {
  /* width: 80%; */
  padding: 0.7rem;
  border: none;
  outline: none;
  border-radius: 1rem;
  margin-right: 2rem;
}
.search_question:focus {
  width: 15rem;
}
.search_container {
  position: relative;
}
.list_searched {
  position: absolute;
  z-index: 6;
  top: 3rem;
  background: white;
  border: 0.1rem solid var(--accent);
  border-radius: 0.4rem;
  width: 15rem;
}
.link_button {
  border: none;
  outline: none;
  background: transparent;
}
</style>
<script>
import axios from "axios";
import { ref, computed, watch, onMounted } from "vue";
import { useRouter } from "vue-router";
export default {
  name: "Search",
  setup() {
    const searchedList = ref(null);
    const router = useRouter();
    const handleSearch = async (value) => {
      const res = await axios(`http://localhost:8000/search/${value}`);
      searchedList.value = res?.data?.searched;
    };
    const handleSearchClick = (id) => {
      router.push({
            name: 'detail', 
            params: { id }
          });
      searchedList.value=null
    }
    return {
      searchedList,
      handleSearch,
      handleSearchClick,
    };
  },
};
</script>