<script>
  import Margin from "../../../components/atoms/Margin.svelte";
  import CommentariesCard from "../../../components/organisms/Cards/commentariesCard.svelte";
  import ProjectInfosCard from "../../../components/organisms/Cards/projectInfosCard.svelte";

  export let data;
</script>

<Margin marginTop='3%'>
  <ProjectInfosCard data={data} />
</Margin>

<CommentariesCard data={data} />