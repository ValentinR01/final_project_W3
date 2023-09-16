<script>
// @ts-nocheck
  import { browser } from '$app/environment';
  import { user } from '../store';
  if (browser) {
    if($user.authentification == "logged in" && $user.role != 'dev'){
      window.location.href = "/projects/dashboard";
    } else if ($user.authentification != "logged in" && $user.role != 'dev') {
      window.location.href = "/login";
    }
  }

  import '../assets/css/global.css';

  import Logo from '../assets/img/logo_color.png';
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
  import InputForm from '../components/molecules/formFields/InputForm.svelte';
  import TextareaForm from '../components/molecules/formFields/TextareaForm.svelte';
  import CheckboxForm from '../components/molecules/formFields/CheckboxForm.svelte';
  import Menu from '../components/molecules/Menu.svelte';
  import Select from '../components/atoms/Select.svelte';
  import SelectForm from '../components/molecules/formFields/SelectForm.svelte'
  import Tabs from '../components/molecules/Tabs.svelte';
  import Modal from '../components/molecules/cards/ModalCard.svelte';
  import RadioForm from '../components/molecules/formFields/RadioForm.svelte';
  import Pagination from '../components/atoms/Pagination.svelte';
  import VideoAction from '../components/molecules/cards/VideoAction.svelte';
  import DownloadIcon from '../assets/icons/DownloadIcon.svelte';
  import EmployeeCard from '../components/molecules/cards/EmployeeCard.svelte';
  import CommentaryCard from '../components/molecules/cards/CommentaryCard.svelte';
  import Header from '../components/organisms/Header.svelte';
  import ModalLinkVideo from '../components/organisms/Modals/ModalLinkVideo.svelte';
  import ModalIntervenor from '../components/organisms/Modals/ModalIntervenor.svelte';
  import SubtitlesRequest from '../components/organisms/Forms/SubtitlesRequest.svelte';
  import CommentaryForm from '../components/organisms/Forms/CommentaryForm.svelte';
  import NewUserForm from '../components/organisms/Forms/NewUserForm.svelte';
  import ProjectEditionForm from '../components/organisms/Forms/ProjectEditionForm.svelte';
  import ProjectCreationForm from '../components/organisms/Forms/ProjectCreationForm.svelte';
  import BioEdition from '../components/organisms/Forms/BioEdition.svelte';
  import RoomRegistrationForm from '../components/organisms/Forms/RoomRegistrationForm.svelte';
  import Table from '../components/organisms/Table.svelte';

  import ProjectComments from '../tabs/Project Details/ProjectComments.svelte';
  import ProjectInfos from "../tabs/Project Details/ProjectInfos.svelte";
  import ProjectTraduction from "../tabs/Project Details/ProjectTraduction.svelte";
  import ProjectVideo from "../tabs/Project Details/ProjectVideo.svelte";
	
	let values;

  export let data;

  // List of tab items with labels, values and assigned components
  let items = [
    { label: "Infos projet",
     value: 1,
     component: ProjectInfos
    },
    { label: "Video",
     value: 2,
     component: ProjectVideo
    },
    { label: "Traductions",
     value: 3,
     component: ProjectTraduction
    },
    { label: "Commentaires",
     value: 4,
     component: ProjectComments
    }
  ];
</script>

{$user.role}
{$user.domain}
{$user.authentification}
<Text
  textTag='h1'
  class='text-preset-1'
  textColor='blue'
  >
  Les atomes
</Text>

<br><br>
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
<br><br>

<TextArea placeholder="Enter your text here..." />
<br><br>
<Input type='email' id='email' name='email' placeholder='Email' required/>
<br><br>
<Input type='password' id='password' name='password' placeholder='Password' required/>
<br><br>
<Select nameSelect="rating" options={data.metadata.rating}/>
<br><br>
<Button> Valider </Button>
<br><br>
<Text textTag='p' class='text-preset-4' textColor='grey'>Already have an account ? <Link class='text--semibold' linkUrl='/login'>Login</Link></Text>
<br><br>
<Icon name="add">
  <AddIcon />
</Icon>
<br><br>
<Icon name="copy" width="20" height="20">
  <CopyIcon />
</Icon>
<br><br>
<Link
  linkUrl='/dashboard'> 
  dashboard
</Link>
<Link
  linkUrl='/account'> 
  <Icon name="user" width="50" height="50"> <UserIcon /> </Icon>
</Link>
<br><br>
<DatePicker />
<br><br>
<Radio values={data.metadata.categorie} cat='categorie'/>
<br><br>
<Checkbox values={data.metadata.instruments} cat='instruments'/>
<br><br>
<!-- Pagination exemple-->
{#if values}
  {#each values as value}
    <p>
    	{value}
    </p>
  {/each}
{/if}
<Pagination rows={data.metadata.instruments} perPage={3} bind:trimmedRows={values} />
<!-- End pagination exemple -->
 
<br><br><br>
<Text
  textTag='h1'
  class='text-preset-1'
  textColor='blue'
  >
  Les molecules
</Text>

<br><br>
<SelectForm nameSelect="role" options={data.metadata.role}>Rôle</SelectForm>
<br><br>
<InputForm id="project" name="project"> Nom du projet </InputForm>
<br><br>
<TextareaForm name='commentaire' placeholder='Enter your text here...'>
  Commentaire
</TextareaForm>
<br><br>

<SelectForm labelName='level' nameSelect="rating" options={data.metadata.rating}> Niveau </SelectForm>
<br><br>
<CheckboxForm data={data.metadata.instruments} catForm='instruments'> Instruments </CheckboxForm>
<br><br>
<RadioForm data={data.metadata.categorie} catForm='categorie'> Type de vidéo </RadioForm>
<br><br><br>
<Rating rate={data.asset[0].rating} />
<br><br>
<Searchbar urlSearchbar="projects" data={data.asset} widthSearchbar="500" />
<br><br>
<Searchbar urlSearchbar="users" data={data.users} widthSearchbar="250" />
<br><br>
<Menu role={data.users[0].role} />
<br><br>
<Tabs {items} data={data}/>
<br><br>
<Modal buttonText='Ouvrir modale'>
  <Text> CONTENU DE LA MODALE </Text>
</Modal>
<br><br>
<VideoAction>
  <DownloadIcon slot='icon' />
  <span slot='text'>Télécharger la vidéo</span>
</VideoAction>
<br><br>
<EmployeeCard employeePicture={data.users[0].profile_pic}>
  <span slot='name'>{data.users[0].fullname}</span>
  <span slot='number-projects'>{data.users[0].count_assigning_asset}</span>
</EmployeeCard>
<br><br>
<EmployeeCard employeePicture={data.users[1].profile_pic}>
  <span slot='name'>{data.users[1].fullname}</span>
  <span slot='number-projects'>{data.users[1].count_assigning_asset}</span>
</EmployeeCard>
<br><br>

<CommentaryCard>
  <span slot='name'>{data.users[1].fullname}</span>
  <span slot='job'>{data.users[1].domain}</span>
  <span slot='date'> 12/06/2023 </span>
  <span slot='comment'> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. </span>
</CommentaryCard>

<br><br><br>
<Text
  textTag='h1'
  class='text-preset-1'
  textColor='blue'
  >
  Les organismes
</Text>

<br><br>
<Table rowElements={data.asset}/>
<br><br>
<Header />
<br><br>
<ModalLinkVideo value='https://jevouspartagemavideo.com/egtyhuhdizhmsjh'/>
<br><br>
<ModalIntervenor type='composer'/>
<br><br>

<!--
<SubtitlesRequest languages={data.metadata.translations} data={data.asset[0].translations} /> 
<br><br>
<CommentaryForm />
<br><br>
<ProjectEditionForm data={data} />
<BioEdition typeBio='composer' />
<RoomRegistrationForm data={data.booking}/>
<ProjectCreationForm data={data} />
<NewUserForm data={data}/>-->
