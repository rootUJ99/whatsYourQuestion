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
    <div class="list_searched">
      <ul class="remove_bullet">
        <li v-for="item in searchedList" :key="item.question">
          <a href="#" class="anchor_decoration">{{ item.question }}</a>
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
  display: none;
  background: white;
  width: 400px;
}
.search_container:hover .list_searched {
  display: block;
}
</style>
<script>
import axios from "axios";
import { ref, computed, watch, onMounted } from "vue";

export default {
  name: "Search",
  setup() {
    const searchedList = ref(null);
    const handleSearch = async (value) => {
      console.log("value", value);
      const res = await axios(`http://localhost:8000/search/${value}`);
      searchedList.value = res?.data?.searched;
    };
    return {
      searchedList,
      handleSearch,
    };
  },
};
</script>