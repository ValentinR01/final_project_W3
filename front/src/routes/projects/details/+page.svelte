<script>
  import Margin from "../../../components/atoms/Margin.svelte";
  import Text from "../../../components/atoms/Text.svelte"; 
  import Tabs from "../../../components/molecules/Tabs.svelte";

  import ProjectComments from "../../../tabs/Project Details/ProjectComments.svelte";
  import ProjectInfos from "../../../tabs/Project Details/ProjectInfos.svelte";
  import ProjectTraduction from "../../../tabs/Project Details/ProjectTraduction.svelte";
  import ProjectVideo from "../../../tabs/Project Details/ProjectVideo.svelte";

  export let data;

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

<Margin marginTop='3%'>
  <div class="project-details card block-center">  
    <div class=''></div>
  
    <Margin marginBottom='40px'>
      <Text
        textTag='h1'
        class='text-preset-2 text--uppercase text-center'
      >
        Nom du projet
      </Text>
    </Margin>
  
    <Tabs {items} {data}/>
  
  </div>
</Margin>

<style>
  .project-details{
    border-top: var(--color-background-quaternary) 45px solid;
  }
</style>