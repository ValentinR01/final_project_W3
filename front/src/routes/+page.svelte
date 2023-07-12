<script>
// @ts-nocheck

  import '../assets/css/global.css';

  import Tab1 from "../tabs/tab1.svelte";
  import Tab2 from "../tabs/tab2.svelte";
  import Tab3 from "../tabs/tab3.svelte";

  import Logo from '../assets/img/logo_color.png'
  import Button from '../components/atoms/Button.svelte';
  import Icon from '../components/atoms/Icon.svelte';
  import TextArea from "../components/atoms/Text-Area.svelte";
  import AddIcon from '../assets/icons/AddIcon.svelte';
  import CopyIcon from '../assets/icons/CopyIcon.svelte';
  import Radio from '../components/atoms/Radio.svelte';
  import Checkbox from '../components/atoms/Checkbox.svelte';
  import Link from '../components/atoms/Link.svelte';
  import DatePicker from '../components/atoms/DatePicker.svelte';
  import UserIcon from '../assets/icons/UserIcon.svelte';
  import Image from '../components/atoms/Image.svelte';
  import Text from '../components/atoms/Text.svelte';
  import Input from '../components/atoms/Input.svelte';

  import Rating from '../components/molecules/Rating.svelte';
  import Searchbar from '../components/molecules/Searchbar.svelte';
  import InputForm from '../components/molecules/InputForm.svelte';
  import TextareaForm from '../components/molecules/TextareaForm.svelte';
  import Menu from '../components/molecules/Menu.svelte';
  import Select from '../components/atoms/Select.svelte';
  import SelectForm from '../components/molecules/SelectForm.svelte';
  import Tabs from '../components/molecules/Tabs.svelte';
  import Modal from '../components/molecules/cards/Modal.svelte';

  import Table from '../components/organisms/Table.svelte';

  export let data;

  // List of tab items with labels, values and assigned components
  let items = [
    { label: "Tab 1",
     value: 1,
     component: Tab1
    },
    { label: "Tab 2",
     value: 2,
     component: Tab2
    },
    { label: "Tab 3",
     value: 3,
     component: Tab3
    }
  ];
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
<br><br>
<!-- <SortArrow /> -->

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

<DatePicker />
<Radio values={data.metadata.categorie} cat='categorie'/>
<Checkbox values={data.metadata.instruments} cat='instruments'/>

<br><br><br>
<Text
  textTag='h1'
  class='text-preset-1'
  textColor='blue'
  >
  Les molecules
</Text>

<br><br>
<Select nameSelect="rating" options={data.metadata.rating}/>
<br>
<SelectForm nameSelect="role" options={data.metadata.role}>Rôle</SelectForm>
<br>
<Rating rate={data.asset[0].rating} />
<br>
<Searchbar urlSearchbar="projects" data={data.asset} widthSearchbar="500" />
<br>
<Searchbar urlSearchbar="users" data={data.users} widthSearchbar="250" />
<br>
<Menu role={data.users[0].role} />
<br>
<InputForm id="project" name="project"> Nom du projet </InputForm>
<br>
<TextareaForm name='commentaire'>Commentaire</TextareaForm>
<br><br>
<Modal buttonText='Ouvrir modale'>
  <Text> CONTENU DE LA MODALE </Text>
</Modal>
<Tabs/>

<br><br><br>
<Text
  textTag='h1'
  class='text-preset-1'
  textColor='blue'
  >
  Les organismes
</Text>
<Table rowElements={data.asset}/>

<br><br>