<script lang="ts">
  /** @type {import('./$types').PageData} */
  import '../assets/css/global.css'
  import Radio from '../components/atoms/Radio.svelte'
  export let data;
</script>

<Radio values={data.project.instruments} cat='instruments'/>
<Radio values={data.project.languages} cat='languages'/>








