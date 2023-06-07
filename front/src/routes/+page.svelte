<script lang="ts">
  /** @type {import('./$types').PageData} */
  import '../assets/css/global.css'
  import Radio from '../components/atoms/Radio.svelte'
  import Checkbox from '../components/atoms/Checkbox.svelte'
  export let data;
</script>

<Radio values={data.project.categorie} cat='categorie'/>

<Checkbox values={data.project.instruments} cat='instruments'/>





