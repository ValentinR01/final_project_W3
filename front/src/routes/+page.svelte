<script lang="ts">
  /** @type {import('./$types').PageData} */
  import '../assets/css/global.css'
  import Radio from '../components/atoms/Radio.svelte'
  export let data;
</script>

<h1> Tous les instruments </h1>
<Radio values={data.project.instruments}/>
<Radio values={data.project.languages}/>








