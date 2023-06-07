<script lang="ts">
  /** @type {import('./$types').PageData} */
  import '../assets/css/global.css';
  import Button from '../components/atoms/Button.svelte';
  import TextArea from "../components/atoms/Text-Area.svelte";
  import Radio from '../components/atoms/Radio.svelte';
  import Checkbox from '../components/atoms/Checkbox.svelte';
  export let data;
</script>

<TextArea />
<Button> Valider </Button>
<Radio values={data.project.categorie} cat='categorie'/>
<Checkbox values={data.project.instruments} cat='instruments'/>

