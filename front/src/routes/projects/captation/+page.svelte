<script>
  import CommentariesCard from "../../../components/organisms/Cards/commentariesCard.svelte";
  import ProjectInfosCard from "../../../components/organisms/Cards/projectInfosCard.svelte";

  export let data;
</script>

<ProjectInfosCard data={data} />

<CommentariesCard data={data} />