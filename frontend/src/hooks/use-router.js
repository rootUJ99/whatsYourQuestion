import { computed, getCurrentInstance } from 'vue';
export const useRouter = () => {
    const vm = getCurrentInstance();
    if (!vm) {
        throw new ReferenceError('Not found vue instance.');
    }
    const route = computed(() => vm.$route);
    return { route, router: vm.$router };
};