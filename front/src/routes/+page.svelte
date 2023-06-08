<script lang="ts">
  /** @type {import('./$types').PageData} */
  import '../assets/css/global.css';
  import Logo from '../assets/img/logo_color.png'
  import Button from '../components/atoms/Button.svelte';
  import Icon from '../components/atoms/Icon.svelte';
  import TextArea from "../components/atoms/Text-Area.svelte";
  import AddIcon from '../assets/icons/AddIcon.svelte';
  import CopyIcon from '../assets/icons/CopyIcon.svelte';
  import Radio from '../components/atoms/Radio.svelte';
  import Checkbox from '../components/atoms/Checkbox.svelte';
  import Link from '../components/atoms/Link.svelte';
  import UserIcon from '../assets/icons/UserIcon.svelte';
  import Image from '../components/atoms/Image.svelte';
  import Text from '../components/atoms/Text.svelte';
  import Input from '../components/atoms/Input.svelte';
  import Rating from '../components/molecules/Rating.svelte';
  import Menu from '../components/molecules/Menu.svelte';
  import InputForm from '../components/molecules/InputForm.svelte';
  import TextareaForm from '../components/molecules/TextareaForm.svelte';

  export let data;
</script>

<Text
  textTag='h1'
  class='text-preset-1'
  textColor='blue'
  >
  Les atomes
</Text>

<Image
  imageSrc={Logo}
  imageAlt="Saline Academie Logo"
  imageWidth=160
/>
<Image
  imageSrc={Logo}
  imageAlt="Saline Academie Logo"
  imageWidth=160
  border
/>
<TextArea />

<Input type='email' id='email' name='email' placeholder='Email' required/>
<Input type='password' id='password' name='password' placeholder='Password' required/>
<Button> Valider </Button>
<Text textTag='p' class='text-preset-4' textColor='grey'>Already have an account ? <Link class='text--semibold' linkUrl='/login'>Login</Link></Text>

<Icon name="add">
  <AddIcon />
</Icon>
<Icon name="copy" width="20" height="20">
  <CopyIcon />
</Icon>

<Link
  linkUrl='/dashboard'> 
  dashboard
</Link>
<Link
  linkUrl='/account'> 
  <Icon name="user" width="50" height="50"> <UserIcon /> </Icon>
</Link>

<Radio values={data.project.categorie} cat='categorie'/>
<Checkbox values={data.project.instruments} cat='instruments'/>

<Text
  textTag='h1'
  class='text-preset-1'
  textColor='blue'
  >
  Les molecules
</Text>

<br>
<Menu role={data.user.role} />
<br>
<Rating rate={data.project.rating} />
<br>
<InputForm id="project" name="project"> Nom du projet </InputForm>
<TextareaForm name='commentaire'>Commentaire</TextareaForm>
