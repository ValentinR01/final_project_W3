<script lang="ts">
  /** @type {import('./$types').PageData} */
  import '../assets/css/global.css';
  import Button from '../components/atoms/Button.svelte';
  import Icon from '../components/atoms/Icon.svelte';
  import TextArea from "../components/atoms/Text-Area.svelte";
  import AddIcon from '../assets/icons/AddIcon.svelte';
  import CopyIcon from '../assets/icons/CopyIcon.svelte';
  import Radio from '../components/atoms/Radio.svelte';
  import Checkbox from '../components/atoms/Checkbox.svelte';
  export let data;
</script>

<TextArea />
<Button> Valider </Button>

<Icon name="add">
  <AddIcon />
</Icon>
<Icon name="copy" width="20" height="20">
  <CopyIcon />
</Icon>

<Radio values={data.project.categorie} cat='categorie'/>
<Checkbox values={data.project.instruments} cat='instruments'/>
