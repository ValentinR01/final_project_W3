<script>
  import '../assets/css/global.css'
  import Button from '../components/atoms/Button.svelte';
  import Icon from '../components/atoms/Icon.svelte';
  import TextArea from "../components/atoms/Text-Area.svelte";
  import AddIcon from '../assets/icons/AddIcon.svelte';
  import CopyIcon from '../assets/icons/CopyIcon.svelte';
</script>

<h1>Welcome to SvelteKit</h1>
<TextArea />
<Button> Valider </Button>

<Icon name="add">
  <AddIcon />
</Icon>
<Icon name="copy" width="20" height="20">
  <CopyIcon />
</Icon>